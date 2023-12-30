import React from 'react';
import { Item } from '../components'
const List = () => {
    const data = [
        { id: 1, name: 'Item 1' },
        { id: 2, name: 'Item 2' },
        { id: 3, name: 'Item 3' },
        { id: 4, name: 'Item 4' },
        { id: 5, name: 'Item 5' },
        { id: 6, name: 'Item 6' },
    ];

    return (
        <div>
            <h1>List Songs</h1>
            <div className="grid grid-cols-4 gap-1">
                {data.map(item => (
                    <Item key={item.id} object={item} />
                ))}
            </div>
        </div>
    );
};

export default List;
