(define (domain LegoWorld2d)
    (:requirements :strips :negative-preconditions :disjunctive-preconditions :conditional-effects)
    (:predicates
        (clear ?row ?col)
        (moveable ?row ?col)
        (occupied ?row ?col)
        (on_ground ?row ?col)
    )
    ; (:derived (occupied ?row ?col)
    ;     and ((not (clear ?row ?col))
    ;     (not (moveable ?row ?col))
    ; )

    (:action move
        :parameters (
            ?old_below_row
            ?old_below_col
            ?old_row
            ?old_col
            ?new_row
            ?new_col
        )
        :precondition (and
            (or (on_ground ?old_row ?old_col) (occupied ?old_below_row ?old_below_col))
            (moveable ?old_row ?old_col)
            (clear ?new_row ?new_col)
        )
        :effect (and
            (when (occupied ?old_below_row ?old_below_col)
                (and
                    (not (occupied ?old_below_row ?old_below_col))
                    (moveable ?old_below_row ?old_below_col)
                )
            )
            (when (on_ground ?old_row ?old_col)
                (and
                    (not (on_ground ?old_row ?old_col))
                    (occupied ?old_row ?old_col)
                )
            )
            ;on ground only applies if occupied
            (not (moveable ?old_row ?old_col))
            (not (clear ?new_row ?new_col))
            (moveable ?new_row ?new_col)
            )
    )
)
