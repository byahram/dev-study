const express = require("express");
const router = express.Router();
const cartController = require("../controllers/cartController");
const authController = require("../controllers/authController");

router.post("/", authController.authenticate, cartController.addItemToCart);
// router.delete(
//   "/:id",
//   authController.authenticate,
//   cartController.deleteCartItem
// );

module.exports = router;
