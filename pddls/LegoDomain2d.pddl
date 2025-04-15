(define (domain LegoWorld2d)
    (:requirements :strips :negative-preconditions)
    (:predicates
        (clear ?row ?col)
        (moveable ?row ?col)
        (occupied ?row ?col)
    )
    
    (:action move
        :parameters (
            ?old_row
            ?old_col
            ?new_row
            ?new_col
        )
        :precondition (and
            (not (clear ?old_row ?old_col))
            (occupied ?old_row ?old_col) 
            (moveable ?old_row ?old_col)
            (clear ?new_row ?new_col)
            (not (occupied ?new_row ?new_col))
            (not (moveable ?new_row ?new_col))
        )
        :effect (and 
            (clear ?old_row ?old_col)
            (not (occupied ?old_row ?old_col))
            (not (moveable ?old_row ?old_col))
            (not (clear ?new_row ?new_col))
            (occupied ?new_row ?new_col)
            (moveable ?new_row ?new_col)
        )
    
    
    
    
    )






)








; (define (domain LegoWorld2d)
;     (:requirements :strips :negative-preconditions :disjunctive-preconditions)
;     (:predicates
;         (clear ?row ?col)
;         ; (supported ?row ?col)
;         (trapped ?row ?col)
;         (occupied ?row ?col)
;     )

;     (:action move
;         :parameters (
;             ?old_row
;             ?old_col
;             ?new_row
;             ?new_col
;         )
;         :precondition (and 
;         (or (not (trapped ?old_row ?old_col)) (trapped ?old_row ?old_col))
;         (occupied ?old_row ?old_col)
;         (clear ?new_row ?new_col)
    
;         ; (supported ?new_row ?new_col)
;         )
;         :effect (and 
;         (not (clear ?new_row ?new_col))
;         (occupied ?new_row ?new_col)
;         (clear ?old_row ?old_col)
;         (not (occupied ?old_row ?old_col))
;         (not (trapped ?new_row ?new_col))
;         )
;     )
; )
