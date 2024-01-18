import React, { useEffect, useState } from "react";
import axios from "axios";
import { Item } from '../components'
const Discover = () => {
  const [characters, setCharacter] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const fetchData = () => {
    return axios.get("https://thronesapi.com/api/v2/Characters")
      .then((response) => { setCharacter(response.data); setIsLoading(false); });

  }
  useEffect(() => {
    setIsLoading(true);
    fetchData();
  }, [])

  return (
    <div>
      {isLoading ?
        <div
          className="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-current border-r-transparent align-[-0.125em] motion-reduce:animate-[spin_1.5s_linear_infinite]"
          role="status">
          <span
            className="!absolute !-m-px !h-px !w-px !overflow-hidden !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]"
          >Loading...</span>
        </div> : null}
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
