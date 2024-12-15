const express = require("express");
const authController = require("../controllers/authController");
const orderController = require("../controllers/orderController");
const router = express.Router();

router.post("/", authController.authenticate, orderController.createOrder);
router.get("/me", authController.authenticate, orderController.getOrder);

module.exports = router;
