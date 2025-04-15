(define (domain LegoWorld2d)
    (:requirements :strips :negative-preconditions :adl :derived-predicates)
    (:predicates
        (clear ?row ?col)
        (supported ?row ?col)
        (trapped ?row ?col)
    )
    (:action move
        :parameters (
            ?old_row
            ?old_col
            ?new_row
            ?new_col
        )
        :precondition (and 
        (not (trapped ?old_row ?old_col))
        (clear ?new_row ?new_col)
        (supported ?new_row ?new_col)
        )
        :effect (and 
        (not (clear ?new_row ?new_col))
        (clear ?old_row ?old_col)
        )
    )
)
