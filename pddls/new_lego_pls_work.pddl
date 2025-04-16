(define (domain plswork)
    (:requirements :strips :negative-preconditions :conditional-effects :numeric-fluents)
    (:predicates
        (moveable ?row ?col)
        (on_ground ?row ?col)
        (clear ?row ?col)
    )
    (:functions
        (block_pos_row ?int)
        (block_pos_col ?int)
    )
    (:action move
        :parameters (
            ?old_row
            ?old_col
            ?new_row
            ?new_col

        )
        :precondition (and 

            (= (block_pos_row ?old_row) ?old_row)
            (= (block_pos_col ?old_col) ?old_col) 
            (= (block_pos_row ?new_row) ?new_row)
            (= (block_pos_col ?new_col) ?new_col) 
            (moveable ?old_row ?old_col)
            (clear ?new_row ?new_col)

        )
        :effect (and 
            (when (on_ground ?old_row ?old_col)
                (and
                (not (moveable ?old_row ?old_col))
                (clear ?old_row ?old_col)
                )
            )
            (when (not (on_ground ?old_row ?old_col))
                (and
                (moveable (- ?old_row 1) ?old_col)
                (clear ?old_row ?old_col)
                (not (moveable ?old_row ?old_col)) 
                )
            )
            (when (on_ground ?new_row ?new_col)
                (and
                (not (clear ?new_row ?new_col))
                (moveable ?new_row ?new_col)
                )
            )
            (when (not (on_ground ?new_row ?new_col))
                (and
                (not (moveable (- ?new_row 1) ?new_col))
                (not (clear ?new_row ?new_col))
                (moveable ?new_row ?new_col)
                )
            )
        )
    )
)