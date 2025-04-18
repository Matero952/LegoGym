(define (domain pleasework)
    (:requirements :strips :negative-preconditions :typing :conditional-effects)
    (:types
        row col
    )
    (:predicates
        (moveable ?row ?col)
        (trapped ?row ?col)
        (is_above ?upper_row ?lower_row)
        (block_at ?row ?col)
        (clear ?row ?col)
    )
    (:action move
        :parameters (
            ?old_row
            ?old_col
            ?new_row
            ?new_col
        )
        :precondition (and 
            (block_at ?old_row ?old_col)
            (moveable ?old_row ?old_col)
            (not (trapped ?old_row ?old_col))

            (not (block_at ?new_row ?new_col))
            (not (moveable ?new_row ?new_col))
            (not (trapped ?new_row ?new_col))
            (clear ?new_row ?new_col)
        )
        :effect (and 
            (not (block_at ?old_row ?old_col))
            (not (moveable ?old_row ?old_col))
            (clear ?old_row ?old_col)

            (block_at ?new_row ?new_col)
            (moveable ?new_row ?new_col)
            (not (clear ?new_row ?new_col))

            (forall (?lower - row) 
                (when (and (is_above ?old_row ?lower)
                    (block_at ?lower ?old_col))

                    (moveable ?lower ?old_col)
                    (not (trapped ?lower ?old_col))
                )
            )
            (forall (?lower - row)
                (when (and (is_above ?new_row ?lower)
                    (block_at ?lower ?new_col))

                    (not (moveable ?lower ?new_col))
                    (trapped ?lower ?new_col)
                )
            )
    )
)