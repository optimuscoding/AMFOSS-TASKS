defmodule FileCopier do
  def copy_file(input_file, output_file) do
    case File.read(input_file) do
      {:ok, content} ->
        case File.write(output_file, content) do
          :ok -> IO.puts("File copied successfully.")
          {:error, reason} -> IO.puts("Failed to write to file: #{reason}")
        end

      {:error, reason} ->
        IO.puts("Failed to read file: #{reason}")
    end
  end
end


FileCopier.copy_file("input.txt", "output.txt")

