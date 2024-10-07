# RestV11RequisitionsGet200ResponseInnerItemPackagesInnerChangeOrderRequest

The change order request an item package is associated with. Only returned on three tier projects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the change order request associated with the item package | [optional] 
**title** | **str** | title of the change order request associated with the item package | [optional] 
**change_order_acronym_number** | **str** | acronym and number for the change order request associated with the item package | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_requisitions_get200_response_inner_item_packages_inner_change_order_request import RestV11RequisitionsGet200ResponseInnerItemPackagesInnerChangeOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11RequisitionsGet200ResponseInnerItemPackagesInnerChangeOrderRequest from a JSON string
rest_v11_requisitions_get200_response_inner_item_packages_inner_change_order_request_instance = RestV11RequisitionsGet200ResponseInnerItemPackagesInnerChangeOrderRequest.from_json(json)
# print the JSON string representation of the object
print(RestV11RequisitionsGet200ResponseInnerItemPackagesInnerChangeOrderRequest.to_json())

# convert the object into a dict
rest_v11_requisitions_get200_response_inner_item_packages_inner_change_order_request_dict = rest_v11_requisitions_get200_response_inner_item_packages_inner_change_order_request_instance.to_dict()
# create an instance of RestV11RequisitionsGet200ResponseInnerItemPackagesInnerChangeOrderRequest from a dict
rest_v11_requisitions_get200_response_inner_item_packages_inner_change_order_request_from_dict = RestV11RequisitionsGet200ResponseInnerItemPackagesInnerChangeOrderRequest.from_dict(rest_v11_requisitions_get200_response_inner_item_packages_inner_change_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


