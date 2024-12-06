const express = require("express");
const productController = require("../controllers/productController");
const authController = require("../controllers/authController");
const router = express.Router();

router.post(
  "/",
  authController.authenticate,
  authController.checkAdminPermission,
  productController.createProduct
);

module.exports = router;
