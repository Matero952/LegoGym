(define (domain LegoWorld2d)
    (:requirements :strips :negative-preconditions)
    (:predicates
        (clear ?row ?col)
        (moveable ?row ?col)
        (occupied ?row ?col)
    )
    ; (:derived (occupied ?row ?col)
    ;     and ((not (clear ?row ?col))
    ;     (not (moveable ?row ?col))
    ; )

    (:action move
        :parameters (
            ?old_row
            ?old_col
            ?new_row
            ?new_col
        )
        :precondition (and
            (not (occupied ?old_row ?old_col))
            (not (occupied ?new_row ?new_col))
            (moveable ?old_row ?old_col)
            (clear ?new_row ?new_col)
        )
        :effect (and
            (clear ?old_row ?old_col)
            (moveable ?new_row ?new_col)
            (not (moveable ?old_row ?old_col))
            (not (clear ?new_row ?new_col))
            )
    )
)
