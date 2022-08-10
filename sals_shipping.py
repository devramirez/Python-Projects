# Sal's Shipping
weight = 4.8
# ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)

#  Ground Premium Shipping

premium_ground_cost = 125.00
print("Ground shipping Premium $", premium_ground_cost)

# Drone Shipping
weight = 4.8
if weight <= 2:
  drone_shipping_cost = weight * 4.50
elif weight <= 6:
  drone_shipping_cost = weight * 9.0
elif weight <= 10:
  drone_shipping_cost = weight * 12.0
else:
  drone_shipping_cost = weight * 14.25
print("Drone shipping Cost $", drone_shipping_cost)
