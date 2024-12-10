const Product = require("../models/Product");

const PAGE_SIZE = 5;
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
    return res.status(200).json({ status: "success", product });
  } catch (err) {
    return res.status(400).json({ status: "fail", message: err.message });
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
    let response = { status: "success" };

    if (page) {
      query = query.skip((page - 1) * PAGE_SIZE).limit(PAGE_SIZE);

      // 최종 몇개 페이지
      // 데이터가 총 몇개 있는지
      const totalItemNum = await Product.find(cond).countDocuments();
      // 데이터 총 개수 / PAGE_SIZE
      const totalPageNum = Math.ceil(totalItemNum / PAGE_SIZE);
      response.totalPageNum = totalPageNum;
    }

    const productList = await query.exec();
    response.data = productList;

    return res.status(200).json(response);
  } catch (err) {
    return res.status(400).json({ status: "fail", message: err.message });
  }
};

// updateProducts
productController.updateProduct = async (req, res) => {
  try {
    const productId = req.params.id;
    const {
      sku,
      name,
      size,
      image,
      price,
      description,
      category,
      stock,
      status,
    } = req.body;
    const product = await Product.findByIdAndUpdate(
      { _id: productId },
      {
        sku,
        name,
        size,
        image,
        price,
        description,
        category,
        stock,
        status,
      },
      { new: true }
    );
    if (!product) throw new Error("item doesn't exist");

    return res.status(200).json({ status: "success", data: product });
  } catch (err) {
    return res.status(400).json({ status: "fail", message: err.message });
  }
};

// deleteProduct
productController.deleteProduct = async (req, res) => {
  try {
    const productId = req.params.id;
    const product = await Product.findByIdAndUpdate(
      { _id: productId },
      { isDeleted: true }
    );
    if (!product) throw new Error("No item found");
    return res.status(200).json({ status: "success" });
  } catch (err) {
    return res.status(400).json({ status: "fail", message: err.message });
  }
};

//
productController.getProductDetail = async (req, res) => {
  try {
    const productId = req.params.id;
    const product = await Product.findById(productId);
    if (!product) throw new Error("No item found");
    return res.status(200).json({ status: "success", data: product });
  } catch (err) {
    return res.status(400).json({ status: "fail", message: err.message });
  }
};

module.exports = productController;
