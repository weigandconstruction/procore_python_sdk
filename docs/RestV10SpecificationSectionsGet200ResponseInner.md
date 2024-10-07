# RestV10SpecificationSectionsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**number** | **str** | Number | [optional] 
**description** | **str** | Description | [optional] 
**label** | **str** | Label | [optional] 
**current_revision_id** | **int** | Current Revision ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_specification_sections_get200_response_inner import RestV10SpecificationSectionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SpecificationSectionsGet200ResponseInner from a JSON string
rest_v10_specification_sections_get200_response_inner_instance = RestV10SpecificationSectionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10SpecificationSectionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_specification_sections_get200_response_inner_dict = rest_v10_specification_sections_get200_response_inner_instance.to_dict()
# create an instance of RestV10SpecificationSectionsGet200ResponseInner from a dict
rest_v10_specification_sections_get200_response_inner_from_dict = RestV10SpecificationSectionsGet200ResponseInner.from_dict(rest_v10_specification_sections_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


