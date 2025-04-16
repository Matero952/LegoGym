(define (domain plswork)
    (:requirements :strips :negative-preconditions :conditional-effects :numeric-fluents :typing)
    (:types row col)
    (:predicates
        (moveable ?row - row ?col - col)
        (on_ground ?row - row ?col - col)
        (clear ?row - row ?col - col)
    )
    (:functions
        (block_pos_row ?r - row)
        (block_pos_col ?c - col)
    )
    (:action move
        :parameters (
            ?old_row
            ?old_col
            ?new_row
            ?new_col

        )
        :precondition (and 
            (moveable ?old_row ?old_col)
            (clear ?new_row ?new_col)
            (= (block_pos_row ?old_row) ?old_row)
            (= (block_pos_col ?old_col) ?old_col) 
            (= (block_pos_row ?new_row) ?new_row)
            (= (block_pos_col ?new_col) ?new_col) 

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