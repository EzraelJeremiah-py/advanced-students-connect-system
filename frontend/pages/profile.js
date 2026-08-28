import { useEffect, useState } from "react";

export default function Profile() {
  const [student, setStudent] = useState(null);
  const [posts, setPosts] = useState([]);
  const [connections, setConnections] = useState([]);

  useEffect(() => {
    async function fetchProfile() {
      try {
        // Replace with your Render backend URL
        const resStudent = await fetch("https://your-render-backend.onrender.com/student/1");
        const studentData = await resStudent.json();
        setStudent(studentData);

        const resPosts = await fetch("https://your-render-backend.onrender.com/posts/1");
        const postsData = await resPosts.json();
        setPosts(postsData);

        const resConnections = await fetch("https://your-render-backend.onrender.com/connections/1");
        const connectionsData = await resConnections.json();
        setConnections(connectionsData);
      } catch (err) {
        console.error("Error fetching profile:", err);
      }
    }
    fetchProfile();
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Student Profile</h1>
      {student && (
        <div>
          <h2>{student.name}</h2>
          <p>Email: {student.email}</p>
        </div>
      )}
      <h3>Posts</h3>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.content}</li>
        ))}
      </ul>
      <h3>Connections</h3>
      <ul>
        {connections.map((conn) => (
          <li key={conn.id}>Connected with Student {conn.connected_id}</li>
        ))}
      </ul>
    </div>
  );
}
