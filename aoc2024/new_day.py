import os
import http.client
import re


def fetch_input_file_with_httpclient(day_number):
    """
    Fetch the input file for the given day using the built-in http.client module.
    """
    cookie_file = "cookie.txt"
    if not os.path.exists(cookie_file):
        print(
            f"Error: {cookie_file} not found. Please create it with your session cookie.")
        return False

    # Read the session cookie
    with open(cookie_file, "r") as file:
        session_cookie = file.read().strip()

    # Prepare the HTTP request
    conn = http.client.HTTPSConnection("adventofcode.com")
    url = f"/2024/day/{day_number}/input"
    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "Python-http.client",
    }

    try:
        # Send the GET request
        conn.request("GET", url, headers=headers)
        response = conn.getresponse()

        # Handle non-200 responses
        if response.status != 200:
            print(f"Error: Failed to fetch input for day {
                  day_number}. HTTP Status: {response.status}")
            return False

        # Save the input to the file
        input_file_path = f"./inputs/{day_number:02d}.in"
        with open(input_file_path, "wb") as input_file:
            input_file.write(response.read())

        print(f"Fetched input for day {
              day_number} and saved to {input_file_path}.")
        return True

    except Exception as e:
        print(f"Error: An exception occurred while fetching input for day {
              day_number}: {e}")
        return False

    finally:
        conn.close()


def main():
    # Step 1: Get the files in `./inputs/*.in`
    input_dir = "./inputs"
    input_files = [f for f in os.listdir(input_dir) if f.endswith(".in")]

    # Step 2: Find the highest numbered file
    numbers = [int(re.search(r"(\d+)", f).group(1))
               for f in input_files if re.search(r"(\d+)", f)]
    highest_number = max(numbers) if numbers else 0

    # Step 3: Calculate the new number and directory
    new_number = highest_number + 1
    new_dir = f"day_{new_number}"

    # Step 4: Check if the day_{number}.go already exists
    go_file_path = os.path.join(new_dir, "solution.go")
    if os.path.exists(go_file_path):
        print(f"Error: The file '{
              go_file_path}' already exists. No changes made.")
        return

    # Step 5: Fetch input file for the new day
    if not fetch_input_file_with_httpclient(new_number):
        return

    # Create the new directory
    os.makedirs(new_dir, exist_ok=True)

    # Step 6: Create the new `day_{number}.go` file
    package_name = f"day_{new_number}"
    go_content = f"""package {package_name}

import (
\t"fmt"
\t"log"
\t"os"
\t"regexp"
\t"strconv"
\t"strings"
)

func Solution() {{
\tfile, err := os.ReadFile("./inputs/{new_number:02d}.in")
\tif err != nil {{
\t\tlog.Fatal(err)
\t}}

\tlines := strings.Split(string(file), "\\n")

\tpart1(lines)
\tpart2(lines)
}}

func part1(input []string) {{
}}

func part2(input []string) {{
}}"""
    with open(go_file_path, "w") as go_file:
        go_file.write(go_content)

    # Step 7: Update `main.go`
    main_file_path = "./main.go"
    if not os.path.exists(main_file_path):
        print("main.go not found. Please ensure it exists in the root directory.")
        return

    with open(main_file_path, "r") as main_file:
        main_content = main_file.read()

    # Comment out existing Solution() calls
    main_content = re.sub(r"(\s+day_\d+\.Solution\(\))", r"//\1", main_content)

    # Add the new package to imports and call Solution()
    import_statement = f'\t"{package_name}"\n'
    solution_call = f"\t{package_name}.Solution()"

    # Update imports
    if "import (" in main_content:
        main_content = re.sub(
            r"(import \()", rf"\1\n{import_statement}", main_content)
    else:
        print("Imports not found in main.go.")
        return

    # Update main function
    main_function_match = re.search(
        r"func main\(\) {([\s\S]*?)}", main_content)
    if main_function_match:
        main_function_body = main_function_match.group(1)
        main_function_body = f"{main_function_body}\n{solution_call}"
        main_content = re.sub(
            r"func main\(\) {([\s\S]*?)}", f"func main() {{{main_function_body}\n}}", main_content)
    else:
        print("main function not found in main.go.")
        return

    # Write back the updated content
    with open(main_file_path, "w") as main_file:
        main_file.write(main_content)

    print(f"Created {new_dir} with {
          go_file_path}, fetched input, and updated main.go.")


if __name__ == "__main__":
    main()

