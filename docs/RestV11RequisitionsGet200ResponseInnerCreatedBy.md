# RestV11RequisitionsGet200ResponseInnerCreatedBy

Login Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Login Information ID | [optional] 
**name** | **str** | User name | [optional] 
**login** | **str** | User email | [optional] 
**company_name** | **str** | User Company name. If the user belongs to a vendor, the vendor name will be returned. | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_requisitions_get200_response_inner_created_by import RestV11RequisitionsGet200ResponseInnerCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11RequisitionsGet200ResponseInnerCreatedBy from a JSON string
rest_v11_requisitions_get200_response_inner_created_by_instance = RestV11RequisitionsGet200ResponseInnerCreatedBy.from_json(json)
# print the JSON string representation of the object
print(RestV11RequisitionsGet200ResponseInnerCreatedBy.to_json())

# convert the object into a dict
rest_v11_requisitions_get200_response_inner_created_by_dict = rest_v11_requisitions_get200_response_inner_created_by_instance.to_dict()
# create an instance of RestV11RequisitionsGet200ResponseInnerCreatedBy from a dict
rest_v11_requisitions_get200_response_inner_created_by_from_dict = RestV11RequisitionsGet200ResponseInnerCreatedBy.from_dict(rest_v11_requisitions_get200_response_inner_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


