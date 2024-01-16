import React from 'react';
import { Item } from '../components'
const List = () => {
    const data = [
        { id: 1, firstName: 'Item 1' },
        { id: 2, firstName: 'Item 2' },
        { id: 3, firstName: 'Item 3' },
        { id: 4, firstName: 'Item 4' },
        { id: 5, firstName: 'Item 5' },
        { id: 6, firstName: 'Item 6' },
    ];

    return (
        <div>
            <h1>List Songs</h1>
            <div className="grid grid-cols-4 mx-6 ">
                {data.map(item => (
                    <Item key={item.id} object={item} />
                ))}
            </div>
        </div>
    );
};

export default List;
