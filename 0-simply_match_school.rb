#!/usr/bin/env ruby

# Check if there is an argument provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Extract the first argument
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /School/

# Match the pattern in the input string
match = input_string.match(pattern)

# Print the result
puts match ? match[0] : ""

