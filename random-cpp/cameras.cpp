#include <cpr/cpr.h>
#include <iostream>

int main()
{
    // Set up the GraphQL query
    std::string query = R"(
        query {
            user(id: 1) {
                name
            }
        }
    )";

    // Send the query to the GraphQL server
    cpr::Response response = cpr::Post(cpr::Url{"https://mygraphqlserver.com/graphql"},
                                       cpr::Body{query},
                                       cpr::Header{{"Content-Type", "application/graphql"}});

    // Check for errors
    if (response.error)
    {
        std::cerr << "Error sending GraphQL query: " << response.error.message << std::endl;
        return 1;
    }

    // Print the response
    std::cout << response.text << std::endl;

    return 0;
}

/*
In this example, we're sending a query to the GraphQL server at https://mygraphqlserver.com/graphql.
We set the Content-Type header to application/graphql to indicate that we're sending a GraphQL query,
and we pass the query string as the request body.

The cpr::Post function sends a POST request to the server with the query as the body. It returns a
cpr::Response object that contains the server's response. We check for errors by looking at the error
field of the response object, and we print the response text to the console.
*/
