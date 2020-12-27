import React, { useState, useEffect, ReactElement } from 'react';
import axios from 'axios';

export default function Home():ReactElement {

    const [state, setState] = useState({response_text: 'null'})
    
    useEffect(() => {
        axios.get('/api/')
          .then(res => setState(res.data));
    }, [])

    console.log(state);
    return (
        <div>
            <h1>{state.response_text}</h1>
        </div>
    )
}