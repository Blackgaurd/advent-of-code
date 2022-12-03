function score(char)
    if 'a' <= char <= 'z'
        return char - 'a' + 1
    end
    char - 'A' + 27
end

function main()
    io = open("day3/input.txt")

    total = 0
    for line in eachline(io)
        mid = length(line) ÷ 2
        c1, c2 = Set(line[1:mid]), Set(line[mid+1:end])

        for char in c1
            if char in c2
                total += score(char)
            end
        end
    end

    println(total)

    close(io)
end

main()