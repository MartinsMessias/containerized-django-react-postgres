import React, { useEffect, useState } from 'react';

interface UserProps {
  username: string;
  email: string;
}

function App() {
  // store users in a new variable
  const [users, setUsers] = useState([]);

  useEffect(() => {
    let fetchData = async () => {
      let response = await fetch('/api/users');
      let json = await response.json();
      setUsers(json);
    }
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Users</h1>
        {users.map((user: UserProps) => <p>
          {user.username} {user.email}
        </p>)}
      </header>
    </div>
  );
}

export default App;
