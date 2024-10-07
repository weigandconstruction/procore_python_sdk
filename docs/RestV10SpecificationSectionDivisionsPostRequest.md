# RestV10SpecificationSectionDivisionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_section_division** | [**SpecificationSectionDivision**](SpecificationSectionDivision.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_specification_section_divisions_post_request import RestV10SpecificationSectionDivisionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SpecificationSectionDivisionsPostRequest from a JSON string
rest_v10_specification_section_divisions_post_request_instance = RestV10SpecificationSectionDivisionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10SpecificationSectionDivisionsPostRequest.to_json())

# convert the object into a dict
rest_v10_specification_section_divisions_post_request_dict = rest_v10_specification_section_divisions_post_request_instance.to_dict()
# create an instance of RestV10SpecificationSectionDivisionsPostRequest from a dict
rest_v10_specification_section_divisions_post_request_from_dict = RestV10SpecificationSectionDivisionsPostRequest.from_dict(rest_v10_specification_section_divisions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


