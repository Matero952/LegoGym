(define (domain LegoWorld)
    (:requirements :strips :negative-preconditions :typing :adl :derived-predicates)
    (:predicates
        (clear)
        (supported)
        (trapped)
        (onground)
    )
    (:derived (supported ?i)
        (onground ?i)
    )
    (:action move
        :parameters (
            ?moveable_space
            ?available_space
        )
        :precondition (and
        (not (trapped ?moveable_space))
        (not (clear ?moveable_space))
        (supported ?available_space)
        (clear ?available_space)
        )
        :effect (and 
        (clear ?moveable_space)
        (not (clear ?available_space))
        )
    )
)





















































(domain (domain Lego2D)
    (:requirements :strips)
    (:predicates
        (ontable ?i - block)
        (clear ?i - block)
        (on ?i - block ?j - block)
        (handempty)
        (holding ?i - block)
    (:types
        (block - object)
        (brick2 plate8 - block)
        ;2 units, 8 units.
    )
    (:action PICK-UP
        :parameters (?i - block)
        :precondition (and
            (ontable ?i)
            (handempty)
            (clear ?i)
            (not (holding ?i))
        )
        :effect (and
            (not (ontable ?i))
            (not (handempty))
            (not (clear ?i))
            (holding ?i)
    )
    (:action STACK
        :parameters (?i - block ?j block)
        :precondition (and
            (holding ?i)
            (clear ?j)
        )
        :effect (and
            (on ?i ?j)
            (not (holding ?i))
            (not (clear ?j))
        )
    )
    (:action PUT-DOWN
        :parameters (?i - block)
        :precondition (and
            (holding ?i)
        )
        :effect (and
            (ontable ?i)
            (handempty)
            (clear ?i)
            (not (holding ?i))
        )
    )
    (:action UNSTACK
        :parameters (?i - block ?j - block)
        :precondition (and
            (on ?i ?j)
            (clear ?i)
            (handempty)
            (not (holding ?i))
        )
        :effect (and
            (not (on ?i ?j))
            (not (clear ?i))
            (not (handempty))
            (holding ?i)
            (clear ?j)
        )
    )
)
    )
)

