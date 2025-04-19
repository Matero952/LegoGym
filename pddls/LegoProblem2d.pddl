(define (problem LegoProblem2d)
    (:domain pleasework)
    (:objects
    r0 r1 r2 r3 r4 - row
    c0 c1 c2 c3 c4 - col
    )
    
    (:init
    (clear r0 c0)(not (block_at r0 c0))(not (moveable r0 c0))(not (trapped r0 c0))(clear r0 c1)(not (block_at r0 c1))(not (moveable r0 c1))(not (trapped r0 c1))(clear r0 c2)(not (block_at r0 c2))(not (moveable r0 c2))(not (trapped r0 c2))(clear r0 c3)(not (block_at r0 c3))(not (moveable r0 c3))(not (trapped r0 c3))(block_at r0 c4)(not (clear r0 c4))(not (moveable r0 c4))(trapped r0 c4)(is_above r1 r0)(clear r1 c0)(not (block_at r1 c0))(not (moveable r1 c0))(not (trapped r1 c0))(clear r1 c1)(not (block_at r1 c1))(not (moveable r1 c1))(not (trapped r1 c1))(clear r1 c2)(not (block_at r1 c2))(not (moveable r1 c2))(not (trapped r1 c2))(clear r1 c3)(not (block_at r1 c3))(not (moveable r1 c3))(not (trapped r1 c3))(block_at r1 c4)(not (clear r1 c4))(not (moveable r1 c4))(trapped r1 c4)(is_above r2 r1)(clear r2 c0)(not (block_at r2 c0))(not (moveable r2 c0))(not (trapped r2 c0))(clear r2 c1)(not (block_at r2 c1))(not (moveable r2 c1))(not (trapped r2 c1))(clear r2 c2)(not (block_at r2 c2))(not (moveable r2 c2))(not (trapped r2 c2))(clear r2 c3)(not (block_at r2 c3))(not (moveable r2 c3))(not (trapped r2 c3))(block_at r2 c4)(not (clear r2 c4))(not (moveable r2 c4))(trapped r2 c4)(is_above r3 r2)(clear r3 c0)(not (block_at r3 c0))(not (moveable r3 c0))(not (trapped r3 c0))(clear r3 c1)(not (block_at r3 c1))(not (moveable r3 c1))(not (trapped r3 c1))(clear r3 c2)(not (block_at r3 c2))(not (moveable r3 c2))(not (trapped r3 c2))(clear r3 c3)(not (block_at r3 c3))(not (moveable r3 c3))(not (trapped r3 c3))(block_at r3 c4)(not (clear r3 c4))(not (moveable r3 c4))(trapped r3 c4)(is_above r4 r3)(clear r4 c0)(not (block_at r4 c0))(not (moveable r4 c0))(not (trapped r4 c0))(clear r4 c1)(not (block_at r4 c1))(not (moveable r4 c1))(not (trapped r4 c1))(clear r4 c2)(not (block_at r4 c2))(not (moveable r4 c2))(not (trapped r4 c2))(clear r4 c3)(not (block_at r4 c3))(not (moveable r4 c3))(not (trapped r4 c3))(block_at r4 c4)(not (clear r4 c4))(moveable r4 c4)(not (trapped r4 c4))
    )
    (:goal
    (and
    (clear r0 c0)(not (block_at r0 c0))(not (moveable r0 c0))(not (trapped r0 c0))(clear r0 c1)(not (block_at r0 c1))(not (moveable r0 c1))(not (trapped r0 c1))(block_at r0 c2)(not (clear r0 c2))(moveable r0 c2)(not (trapped r0 c2))(block_at r0 c3)(not (clear r0 c3))(not (moveable r0 c3))(trapped r0 c3)(clear r0 c4)(not (block_at r0 c4))(not (moveable r0 c4))(not (trapped r0 c4))(is_above r1 r0)(clear r1 c0)(not (block_at r1 c0))(not (moveable r1 c0))(not (trapped r1 c0))(clear r1 c1)(not (block_at r1 c1))(not (moveable r1 c1))(not (trapped r1 c1))(clear r1 c2)(not (block_at r1 c2))(not (moveable r1 c2))(not (trapped r1 c2))(block_at r1 c3)(not (clear r1 c3))(not (moveable r1 c3))(trapped r1 c3)(clear r1 c4)(not (block_at r1 c4))(not (moveable r1 c4))(not (trapped r1 c4))(is_above r2 r1)(clear r2 c0)(not (block_at r2 c0))(not (moveable r2 c0))(not (trapped r2 c0))(clear r2 c1)(not (block_at r2 c1))(not (moveable r2 c1))(not (trapped r2 c1))(clear r2 c2)(not (block_at r2 c2))(not (moveable r2 c2))(not (trapped r2 c2))(block_at r2 c3)(not (clear r2 c3))(not (moveable r2 c3))(trapped r2 c3)(clear r2 c4)(not (block_at r2 c4))(not (moveable r2 c4))(not (trapped r2 c4))(is_above r3 r2)(clear r3 c0)(not (block_at r3 c0))(not (moveable r3 c0))(not (trapped r3 c0))(clear r3 c1)(not (block_at r3 c1))(not (moveable r3 c1))(not (trapped r3 c1))(clear r3 c2)(not (block_at r3 c2))(not (moveable r3 c2))(not (trapped r3 c2))(block_at r3 c3)(not (clear r3 c3))(moveable r3 c3)(not (trapped r3 c3))(clear r3 c4)(not (block_at r3 c4))(not (moveable r3 c4))(not (trapped r3 c4))(is_above r4 r3)(clear r4 c0)(not (block_at r4 c0))(not (moveable r4 c0))(not (trapped r4 c0))(clear r4 c1)(not (block_at r4 c1))(not (moveable r4 c1))(not (trapped r4 c1))(clear r4 c2)(not (block_at r4 c2))(not (moveable r4 c2))(not (trapped r4 c2))(clear r4 c3)(not (block_at r4 c3))(not (moveable r4 c3))(not (trapped r4 c3))(clear r4 c4)(not (block_at r4 c4))(not (moveable r4 c4))(not (trapped r4 c4))
    )
    )
    )
