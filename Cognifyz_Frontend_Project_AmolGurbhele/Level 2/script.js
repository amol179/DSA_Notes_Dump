// Fetch data from JSONPlaceholder API
document.addEventListener("DOMContentLoaded", () => {
    const postsContainer = document.getElementById("posts-container");

    // Fetch posts data
    fetch("https://jsonplaceholder.typicode.com/posts")
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(posts => {
            // Display posts in the DOM
            posts.slice(0, 10).forEach(post => {
                const postElement = document.createElement("div");
                postElement.classList.add("post");
                postElement.innerHTML = `
                    <h3>${post.title}</h3>
                    <p>${post.body}</p>
                `;
                postsContainer.appendChild(postElement);
            });
        })
        .catch(error => {
            console.error("Failed to fetch posts:", error);
            postsContainer.innerHTML = `<p>Failed to load posts. Please try again later.</p>`;
        });
});
