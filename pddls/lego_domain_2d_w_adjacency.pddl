(define (domain LegoWorld2dAdjacency)
    (:requirements :strips :negative-preconditions :conditional-effects :equality)
    (:predicates
        (moveable ?row ?col)
        (trapped ?row ?col)
        (clear ?row ?col)
        (is_above ?top_row ?top_col ?bot_row ?bot_col)
        (on_ground ?row ?col)
    )
    (:functions
        (row ?cell)
        (col ?cell)
    )
    (:action move
        :parameters (
            ; ?old_below_row 
            ; ?old_below_col
            ?old_row 
            ?old_col
            ; ?new_below_row
            ; ?new_below_col
            ?new_row 
            ?new_col
        )
        :precondition (and 
            (moveable ?old_row ?old_col)
            (clear ?new_row ?new_col)
        )
        :effect (and

            (when (and (not (= ?new_col ?old_col))
                (trapped ?old_below_row ?old_below_col))
                (and 
                (not (trapped ?old_below_row ?old_below_col))
                (not (is_above ?old_row ?old_col ?old_below_row ?old_below_col)) 
                (moveable ?old_below_row ?old_below_col)
                )
            ) 

            (when (and (not (= ?new_col ?old_col)) 
                (moveable ?new_below_row ?new_below_col))
                (and 
                (not (moveable ?new_below_row ?new_below_col))
                (trapped ?new_below_row ?new_below_col))
                (is_above ?new_row ?new_col ?new_below_row ?new_below_col)
                )

            (when (and (not (= ?new_col ?old_col))
                (on_ground ?new_row ?new_col))
                (on_ground ?new_row ?new_col)
            )

            (when (not (= ?new_col ?old_col))
                (and
                (clear ?old_row ?old_col)
                (not (moveable ?old_row ?old_col))
                (not (clear ?new_row ?new_col))
                (moveable ?new_row ?new_col))
            
            )
            
            
            
            )


            

        )
    ) 
 
