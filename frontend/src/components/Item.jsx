const Item  = (props)  => {
    return (
        <div className="flex items-center justify-center">


            <a className="hover:bg-gray-700 delay-50 duration-100 bg-gray-800 p-5 rounded-lg w-60 group" href="">


                <img src="https://picsum.photos/250/250" className="w-full rounded shadow" />


                <h3 className="text-gray-200 font-bold mt-5">{props.object.name}</h3>


                <p className="text-gray-400 font-light mt-2 text-xs"> Your daily update of the most played track from around the world...</p>

            </a>

        </div>);
};

export default Item;
