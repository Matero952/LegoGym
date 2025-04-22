;um here we can just do a direct difficulty step up and make options between dfiferent types of cooked eggs and maybe add oven logic.
(define (domain medium_egg_kitchen)
    (:requirements :strips :typing :negative-preconditions :numeric-fluents)
    (:types
        egg station
    )
    (:predicates
        (cracked ?egg - egg)
        (seasoned ?egg - egg)
        (over_easy ?egg - egg)
        (over_medium ?egg - egg)
        (over_hard ?egg - egg)
        (clean_station ?station - station)
    )
    (:functions
        (cook_time)
    )
    (:action crack_egg
        :parameters (
            ?egg - egg
            ?station - station
        )
        :precondition (and 
            (not (cracked ?egg))
            (clean_station ?station)
        )
        :effect (and 
            (cracked ?egg)
        )
    )
    (:action season_egg
        :parameters (
            ?egg
        )
        :precondition (and 
            (cracked ?egg)
            (not (seasoned ?egg))
        )
        :effect (and 
            (seasoned ?egg)
        )
    
    )
    (:action cook_egg
        :parameters (
            ?egg - egg
            ?station - station
            ?cook_time
        )
        :precondition (and 
            (cracked ?egg)
            (seasoned ?egg)
            (clean_station ?station)
        )
        :effect (and 
            (assign (cook_time ?cook_time) ?cook_time)
            (when (<= (cook_time) 5)
                (over_easy ?egg)
            )
            (when ())
        )
    )
)