import { useEffect, useState } from "react";

export default function Feed() {
  const [feed, setFeed] = useState([]);

  useEffect(() => {
    async function fetchFeed() {
      try {
        // Replace with your Render backend URL
        const res = await fetch("https://your-render-backend.onrender.com/feed/");
        const data = await res.json();
        setFeed(data.feed);
      } catch (err) {
        console.error("Error fetching feed:", err);
      }
    }
    fetchFeed();
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Advanced Students Connect System</h1>
      <h2>Feed</h2>
      <ul>
        {feed.map((item, index) => (
          <li key={index}>
            {item.type === "post" ? (
              <div>
                <strong>Post:</strong> {item.content} (by Student {item.author})
              </div>
            ) : (
              <div>
                <strong>Reshare:</strong> Post {item.post_id} reshared by Student {item.student_id}
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
