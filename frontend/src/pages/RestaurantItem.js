function RestaurantItem(args) {
  const { restaurant, value } = args;

  return (
    <li className="restaurant_item" id={"l" + value}>
      <div className="restaurant_item_checkbox">
        <input id={"i" + value} type="checkbox" />
        <label htmlFor={"i" + value}></label>
      </div>
      <h1 className="restaurant_item_item-detail">{restaurant}</h1>
    </li>
  );
}
export default RestaurantItem;
