(define (domain LegoWorld2dAdjacency)
    (:requirements :strips :negative-preconditions :disjunctive-preconditions :conditional-effects :equality)
    (:predicates
        (moveable ?row ?col)
        (trapped ?row ?col)
        (clear ?row ?col)
        (is_above ?top_row ?top_col ?bot_row ?bot_col)
        (on_ground ?row ?col)
    )
    (:action move
        :parameters (
            ?old_below_row ?old_below_col
            ?old_row ?old_col
            ?new_row ?new_col
        )
        :precondition (and 
            (or (trapped ?old_below_row ?old_below_col) 
                (on_ground ?old_row ?old_col))

            (or(is_above ?old_row ?old_col ?old_below_row ?old_below_col) 
                (on_ground ?old_row ?old_col))          
            
            (moveable ?old_row ?old_col)
            (clear ?new_row ?new_col)
        )
        :effect (and 
            (when (and 
                    (not (and (= ?new_row ?old_row) (= ?new_col ?old_col)))
                    (trapped ?old_below_row ?old_below_col)
                )
                (not (trapped ?old_below_row ?old_below_col))
                (moveable ?old_below_row ?old_below_col)
                (not (is_above ?old_row ?old_col ?old_below_row ?old_below_col)) 
            )

            (when (and 
                    (not (and (= ?new_row ?old_row) (= ?new_col ?old_col)))
                    (on_ground ?old_row ?old_col)
                )
                (not (on_ground ?old_row ?old_col))
                (clear ?old_row ?old_col)
                (not (moveable ?old_row ?old_col))  
            )
            (when (not(and (= ?new_row ?old_row) (= ?new_col ?old_col)))
                (clear ?old_row ?old_col)
                (not (moveable ?old_row ?old_col))
                (not (clear ?new_row ?new_col))
                (moveable ?new_row ?new_col)            
            )
        )
    ) 
) 
