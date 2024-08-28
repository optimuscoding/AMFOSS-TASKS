defmodule DiamondPattern do
  def read_number_from_file(filename) do
    case File.read(filename) do
      {:ok, content} ->
        content
        |> String.trim()
        |> Integer.parse()
        |> case do
          {number, ""} when number > 0 -> {:ok, number}
          _ -> {:error, "Invalid number or empty content"}
        end

      {:error, _reason} -> {:error, "Error reading from file"}
    end
  end

  def write_diamond_to_file(filename, n) do
    if n < 1 or rem(n, 2) == 0 do
      File.write(filename, "Please enter a positive odd number.\n")
    else
      diamond_pattern = generate_diamond(n)
      File.write(filename, diamond_pattern)
    end
  end

  defp generate_diamond(n) do
    half = div(n, 2)

    top_half =
      for i <- 0..half do
        spaces = String.duplicate(" ", half - i)
        stars = String.duplicate("*", 2 * i + 1)
        spaces <> stars <> "\n"
      end

    bottom_half =
      for i <- (half + 1)..(n - 1) do
        spaces = String.duplicate(" ", i - half)
        stars = String.duplicate("*", 2 * (n - i - 1) + 1)
        spaces <> stars <> "\n"
      end

    Enum.join(top_half ++ bottom_half)
  end

  def main do
    input_filename = "input.txt"
    output_filename = "output.txt"

    case read_number_from_file(input_filename) do
      {:ok, n} -> write_diamond_to_file(output_filename, n)
      {:error, message} -> IO.puts(message)
    end
  end
end


DiamondPattern.run()
