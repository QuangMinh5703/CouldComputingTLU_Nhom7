import React from 'react'
import showStore from '../stores/showStore'
import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import Header from '../components/Header';


export default function Show() {
    const store = showStore()
    const [test,setTest] = useState()
    const params = useParams()
    useEffect(() => {
      hanldeFetch()
    },[])
    const hanldeFetch = async () => {
      const res = await  store.fetchData(params.id)
      setTest(res.data) 
      return () => {
        store.reset();
      }
    }
    console.log("test",test);
    //if(!store.data) return <></>
    return (
      <div>
        <Header back/>
        <header className='show-header'>
          <img src={test?.image.large}/>
          <h2>
            {test?.name} ({test?.symbol})
          </h2>
        </header>
        <div className='width'>
          <div className='show-graph'>
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart
                data={store.graphData}
                margin={{
                  top: 10,
                  right: 30,
                  left: 0,
                  bottom: 0,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="Date" />
                <YAxis />
                <Tooltip />
                <Area type="monotone" dataKey="Price" stroke="#8884d8" fill="#8884d8" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
        <div className='show-details'>
          <div className='width'>
            <h2>Details</h2>
            <div className='show-details-row'>
              <h3>Mark cap rank</h3>
              <span>{test?.market_cap_rank}</span>
            </div>
            <div className='show-details-row'>
              <h3>24h high</h3>
              <span>{test?.market_data.high_24h.usd}</span>
            </div>
            <div className='show-details-row'>
              <h3>24h low</h3>
              <span>{test?.market_data.low_24h.usd}</span>
            </div>
            <div className='show-details-row'>
              <h3>Circulating supply</h3>
              <span>{test?.market_data.circulating_supply}</span>
            </div>
            <div className='show-details-row'>
              <h3>Current price</h3>
              <span>{test?.market_data.current_price.usd}</span>
            </div>
          </div>
        </div>
       
      </div>
    );
}
