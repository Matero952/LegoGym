;Objectives:
;1.)Basic Ingredients like Eggs Salt Pepper I dont know 
;2.)Basic Dishes Sacrambled Eggs
;3.)Basic Actions Crack Egg Shake the salt shaker yk and pepper shaker
(define (domain egg_kitchen_test)
    (:requirements :strips :typing :negative-preconditions)
    (:types
        egg
    )
    (:predicates
        (cracked ?egg - egg)
        (salted ?egg - egg)
        (peppered ?egg - egg)
        (cooked ?egg - egg)    
    )
    (:action crack_egg
        :parameters (?egg - egg)
        :precondition (and
            (not (cracked ?egg))
            (not (salted ?egg ))
            (not (peppered ?egg))
        )
        :effect (and
            (cracked ?egg)
        )
    )
    (:action season_egg
        :parameters (
            ?cracked_egg - egg
        )
        :precondition (and 
            (cracked ?cracked_egg)
            (not (salted ?cracked_egg))
            (not (peppered ?cracked_egg))
            (not (cooked ?cracked_egg))
        )
        :effect (and 
            (salted ?cracked_egg)
            (peppered ?cracked_egg)
        )
    )
    (:action cook_egg
        :parameters (
            ?seasoned_egg - egg
        )
        :precondition (and 
            (salted ?seasoned_egg)
            (peppered ?seasoned_egg)
            (not (cooked ?seasoned_egg))
        )
        :effect (and 
            (cooked ?seasoned_egg)
        )
    )
)