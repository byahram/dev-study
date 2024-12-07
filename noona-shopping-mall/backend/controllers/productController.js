const Product = require("../models/Product");

const productController = {};

// createProduct
productController.createProduct = async (req, res) => {
  try {
    const {
      sku,
      name,
      size,
      image,
      category,
      description,
      price,
      stock,
      status,
    } = req.body;
    const product = new Product({
      sku,
      name,
      size,
      image,
      category,
      description,
      price,
      stock,
      status,
    });
    await product.save();
    res.status(200).json({ status: "success", product });
  } catch (err) {
    res.status(400).json({ status: "fail", message: err.message });
  }
};

// getProducts
productController.getProducts = async (req, res) => {
  // $option: "i" 소문자 대문자 구별 nope
  try {
    const { page, name } = req.query;
    const cond = name
      ? { name: { $regex: name, $options: "i" }, isDeleted: false }
      : { isDeleted: false };

    let query = Product.find(cond);
    const productList = await query.exec();
    res.status(200).json({ status: "success", data: productList });
  } catch (err) {
    res.status(400).json({ status: "fail", error: err.message });
  }
};

module.exports = productController;
