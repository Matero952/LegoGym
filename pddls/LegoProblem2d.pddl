(define (problem LegoProblem2d)
    (:domain pleasework)
    (:objects
    r0 r1 r2 r3 r4 - row
    c0 c1 c2 c3 c4 - col
    )
    
    (:init
    (block_at r0 c0)(not (clear r0 c0))(not (moveable r0 c0))(trapped r0 c0)(block_at r0 c1)(not (clear r0 c1))(not (moveable r0 c1))(trapped r0 c1)(clear r0 c2)(not (block_at r0 c2))(not (moveable r0 c2))(not (trapped r0 c2))(is_above r1 r0)(block_at r1 c0)(not (clear r1 c0))(moveable r1 c0)(not (trapped r1 c0))(block_at r1 c1)(not (clear r1 c1))(not (moveable r1 c1))(trapped r1 c1)(clear r1 c2)(not (block_at r1 c2))(not (moveable r1 c2))(not (trapped r1 c2))(is_above r2 r1)(clear r2 c0)(not (block_at r2 c0))(not (moveable r2 c0))(not (trapped r2 c0))(block_at r2 c1)(not (clear r2 c1))(moveable r2 c1)(not (trapped r2 c1))(clear r2 c2)(not (block_at r2 c2))(not (moveable r2 c2))(not (trapped r2 c2))
    )
    (:goal
    (and
    (block_at r0 c0)(not (clear r0 c0))(moveable r0 c0)(not (trapped r0 c0))(block_at r0 c1)(not (clear r0 c1))(not (moveable r0 c1))(trapped r0 c1)(block_at r0 c2)(not (clear r0 c2))(not (moveable r0 c2))(trapped r0 c2)(is_above r1 r0)(clear r1 c0)(not (block_at r1 c0))(not (moveable r1 c0))(not (trapped r1 c0))(block_at r1 c1)(not (clear r1 c1))(moveable r1 c1)(not (trapped r1 c1))(block_at r1 c2)(not (clear r1 c2))(moveable r1 c2)(not (trapped r1 c2))(is_above r2 r1)(clear r2 c0)(not (block_at r2 c0))(not (moveable r2 c0))(not (trapped r2 c0))(clear r2 c1)(not (block_at r2 c1))(not (moveable r2 c1))(not (trapped r2 c1))(clear r2 c2)(not (block_at r2 c2))(not (moveable r2 c2))(not (trapped r2 c2))
    )
    )
    )
