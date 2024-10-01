import { useEffect, useState } from "react";
import axios from "axios";

function MyComponent() {
  URL = "http://localhost:8000/hotels/Алтай";

  const [hotels, setHotels] = useState([]);

  useEffect(() => {
    axios
      .get(URL, { params: { date_from: "2023-03-03", date_to: "2023-03-05" } })
      .then((response) => {
        setHotels(response.data);
      });
  }, []);

  return (
    <div>
      <h1>ОТЕЛИ</h1>
      {hotels &&
        hotels.map((hotel) => {
          return (
            <>
              <h3>{hotel.name}</h3>
              <p>{hotel.lovation}</p>
            </>
          );
        })}
    </div>
  );
}
export default MyComponent;
