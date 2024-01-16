import React, { useEffect, useState } from "react";
import axios from "axios";
import { Item } from '../components'
const Discover = () => {
  const [characters, setCharacter] = useState([]);
  const fetchData = () => {
    return axios.get("https://thronesapi.com/api/v2/Characters")
      .then((response) => setCharacter(response.data));
  }
  useEffect(() => {
    fetchData();
  },[])

  return (
    <div>
      <h1>List Songs</h1>
      <div className="grid grid-cols-4 mx-6 ">
        {characters.map(item => (
          <Item key={item.id} object={item} />
        ))}
      </div>
    </div>
  );
};

export default Discover;
