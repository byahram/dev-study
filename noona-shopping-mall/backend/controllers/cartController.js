const mongoose = require("mongoose");

const Cart = require("../models/Cart");
const cartController = {};

// addItemToCart
cartController.addItemToCart = async (req, res) => {
  try {
    const { userId } = req;
    const { productId, size, qty } = req.body;
    const objectProductId = new mongoose.Types.ObjectId(productId);

    // 유저를 가지고 카트 찾기
    let cart = await Cart.findOne({ userId });

    // 유저가 만든 카트가 없다면 만들어주기
    if (!cart) {
      cart = new Cart({ userId });
      await cart.save();
    }
    // 이미 카트에 들어가있는 아이템이냐? productId, size
    const existItem = cart.items.find((item) => {
      return item.productId.equals(objectProductId) && item.size === size;
    });

    // 카트에 들어가있으면 ("이미 아이템이 카트에 있습니다");
    if (existItem) {
      throw new Error("아이템이 이미 카트에 담겨 있습니다!");
    }

    // 아니면 카트에 아이템을 추가
    cart.items = [...cart.items, { productId, size, qty }];
    await cart.save();

    return res
      .status(200)
      .json({ status: "success", data: cart, cartItemQty: cart.items.length });
  } catch (err) {
    return res.status(400).json({ status: "fail", message: err.message });
  }
};

module.exports = cartController;
