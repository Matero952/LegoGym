(domain (domain Lego3D)
    (:requirements :strips)
    (:predicates
        (ontable ?i - brick)
        (on ?i - brick ?j - brick)
        (clear ?i - brick)
        (at ?i - brick ?p - position)
        (available ?p - position)
        (handempty)
        (holding ?i - brick)
    )
    (:types
        (position - object)
        (brick - object)
        ;Assume that bricks are 1x1
    )
    (:derived (available ?p - position)
        (not (exists (?b - brick) (at ?b ?p)))
    )
    (:action PICKUP
        :parameters (?i - block, ?p - position)
        :precondition (and
        (ontable ?i)
        (clear ?i)
        (handempty)
        (at ?i ?p)
        )
        :effect (and
        (not (ontable ?i))
        (not (clear ?i))
        (not (handempty))
        (not (at ?i ?p))
        (holding ?i)
        )
    )
    (:action PUTDOWN
        :parameters (?i - block, ?p - position)
        :precondition (and
            (holding ?i)
            (available ?p)
        )
        :effect (and
            (not (holding ?i))
            (ontable ?i)
            (at ?i ?p)
        )
    )

    (:action STACK
        :parameters (?i - brick ?j - brick ?p - position)
        :precondition (and
            (clear ?j)
            (available ?p)
            (holding ?i)
        )
        :effect (and
            (not (clear ?j))
            (not (holding ?i))
            (on ?i ?j)
            (at ?i ?p)
        )
    )
    (:action UNSTACK
        :parameters(?i - brick ?j - brick ?p - position)
        :precondition (and
            (handempty)
            (on ?i ?j)
            (at ?i ?p)
            (clear ?i)
        )
        :effect (and
            (not (handempty))
            (not (on ?i ?j))
            (not (at ?i ?p))
            (not (clear ?i))
            (holding ?i)
        )
    )
    (:functions
        (max-block-height)
    )
)

















