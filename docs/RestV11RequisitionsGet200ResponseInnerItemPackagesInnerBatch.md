# RestV11RequisitionsGet200ResponseInnerItemPackagesInnerBatch

The change order batch an item package is associated with. Only returned on multi tier projects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the change order batch associated with the item package | [optional] 
**title** | **str** | title of the change order batch associated with the item package | [optional] 
**change_order_acronym_number** | **str** | acronym and number for the change order batch associated with the item package | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_requisitions_get200_response_inner_item_packages_inner_batch import RestV11RequisitionsGet200ResponseInnerItemPackagesInnerBatch

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11RequisitionsGet200ResponseInnerItemPackagesInnerBatch from a JSON string
rest_v11_requisitions_get200_response_inner_item_packages_inner_batch_instance = RestV11RequisitionsGet200ResponseInnerItemPackagesInnerBatch.from_json(json)
# print the JSON string representation of the object
print(RestV11RequisitionsGet200ResponseInnerItemPackagesInnerBatch.to_json())

# convert the object into a dict
rest_v11_requisitions_get200_response_inner_item_packages_inner_batch_dict = rest_v11_requisitions_get200_response_inner_item_packages_inner_batch_instance.to_dict()
# create an instance of RestV11RequisitionsGet200ResponseInnerItemPackagesInnerBatch from a dict
rest_v11_requisitions_get200_response_inner_item_packages_inner_batch_from_dict = RestV11RequisitionsGet200ResponseInnerItemPackagesInnerBatch.from_dict(rest_v11_requisitions_get200_response_inner_item_packages_inner_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


