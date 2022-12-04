function main()
    io = open("day4/input.txt")

    ans = 0
    for line in eachline(io)
        a, b, c, d = map(x -> parse(Int, x), split(line, ('-', ',')))
        if a <= c && b >= d
            ans += 1
        elseif a >= c && b <= d
            ans += 1
        end
    end
    println(ans)

    close(io)
end

main()