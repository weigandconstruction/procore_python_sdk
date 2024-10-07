# RestV11RequisitionsGet200ResponseInnerItemPackagesInner

Requisition (Subcontractor Invoice) item package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the item package | [optional] 
**contract_id** | **int** | ID of the contract associated with the item package | [optional] 
**change_order_id** | **int** | ID of the change order associated with the item package | [optional] 
**number** | **str** | number associated with the item package&#39;s parent entity | [optional] 
**title** | **str** | title associated with the item package&#39;s parent entity | [optional] 
**status** | **str** | status associated with the item package&#39;s parent entity | [optional] 
**position** | **int** | position associated with the item package&#39;s parent entity | [optional] 
**change_order_acronym_number** | **str** | acronym for the change order object associated with the item package. Null if the item package&#39;s parent entity is a contract. | [optional] 
**change_order_request** | [**RestV11RequisitionsGet200ResponseInnerItemPackagesInnerChangeOrderRequest**](RestV11RequisitionsGet200ResponseInnerItemPackagesInnerChangeOrderRequest.md) |  | [optional] 
**batch** | [**RestV11RequisitionsGet200ResponseInnerItemPackagesInnerBatch**](RestV11RequisitionsGet200ResponseInnerItemPackagesInnerBatch.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_requisitions_get200_response_inner_item_packages_inner import RestV11RequisitionsGet200ResponseInnerItemPackagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11RequisitionsGet200ResponseInnerItemPackagesInner from a JSON string
rest_v11_requisitions_get200_response_inner_item_packages_inner_instance = RestV11RequisitionsGet200ResponseInnerItemPackagesInner.from_json(json)
# print the JSON string representation of the object
print(RestV11RequisitionsGet200ResponseInnerItemPackagesInner.to_json())

# convert the object into a dict
rest_v11_requisitions_get200_response_inner_item_packages_inner_dict = rest_v11_requisitions_get200_response_inner_item_packages_inner_instance.to_dict()
# create an instance of RestV11RequisitionsGet200ResponseInnerItemPackagesInner from a dict
rest_v11_requisitions_get200_response_inner_item_packages_inner_from_dict = RestV11RequisitionsGet200ResponseInnerItemPackagesInner.from_dict(rest_v11_requisitions_get200_response_inner_item_packages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


