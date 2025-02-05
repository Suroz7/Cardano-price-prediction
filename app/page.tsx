"use client"; 

import { useEffect, useState } from "react";
import axios from "axios";
import { Button } from "./components/ui/button";
import { Card, CardContent } from "./components/ui/card";
import { Loader } from "lucide-react";

export default function Home() {
  const [adaData, setAdaData] = useState<any>(null);
  const [loading, setLoading] = useState(false); // Initially not loading
  const [hasStartedPrediction, setHasStartedPrediction] = useState(false); // State to track if prediction has started
  const [formattedPrediction, setFormattedPrediction] = useState<string>("");

  // Function to fetch data when the button is pressed
  const fetchData = async () => {
    setLoading(true);
    setHasStartedPrediction(true); // Update to reflect that prediction request started
    try {
      const response = await axios.get("http://127.0.0.1:5000/api/ada-data");
      setAdaData(response.data);

      // Filter out the <think> text and format it into separate lines
      const predictionText = response.data.prediction.response;
      const formattedText = predictionText.replace(/<think>/g, "\n<think>").split("\n").join("\n\n");

      setFormattedPrediction(formattedText); // Set formatted prediction text
    } catch (error) {
      console.error("Error fetching data:", error);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white p-4">
      <h1 className="text-3xl font-bold mb-4">ADA/USDT Price Predictor</h1>

      {/* If prediction hasn't started, show the intro text and the button */}
      {!hasStartedPrediction ? (
        <div className="flex flex-col items-center">
          <p className="text-lg mb-4">Welcome to the ADA/USDT Price Prediction App! Press the button below to get the latest price and prediction data.</p>
          <Button className="mt-4" onClick={fetchData}><p className="refresh">Start Prediction</p></Button>
        </div>
      ) : (
        // Once prediction starts or has been fetched, show the data and loading spinner
        <>
          {loading ? (
            <Loader className="animate-spin text-blue-500" size={32} />
          ) : (
            <>
              <Card className="p-6 bg-gray-800 text-white w-full max-w-md">
                <CardContent>
                  <p className="text-lg">Live Price: ${adaData?.live_data?.binance?.price}</p>
                  <p className="text-sm">24h Change: {adaData?.live_data?.binance?.percent_change_24h}%</p>
                  <p className="text-sm">Volume: {adaData?.live_data?.binance?.volume}</p>
                </CardContent>
              </Card>

              <Card className="p-6 bg-gray-700 text-white mt-4 w-full max-w-md">
                <CardContent>
                  <h2 className="text-xl font-semibold">Prediction</h2>
                  <p className="text-lg whitespace-pre-line">{formattedPrediction}</p> {/* Display formatted prediction */}
                </CardContent>
              </Card>

              <Button className="mt-4" onClick={fetchData}><p className="refresh">Refresh Data</p></Button>
            </>
          )}
        </>
      )}
    </div>
  );
}