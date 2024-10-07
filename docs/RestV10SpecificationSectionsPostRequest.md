# RestV10SpecificationSectionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_section** | [**RestV10SpecificationSectionsPostRequestSpecificationSection**](RestV10SpecificationSectionsPostRequestSpecificationSection.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_specification_sections_post_request import RestV10SpecificationSectionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SpecificationSectionsPostRequest from a JSON string
rest_v10_specification_sections_post_request_instance = RestV10SpecificationSectionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10SpecificationSectionsPostRequest.to_json())

# convert the object into a dict
rest_v10_specification_sections_post_request_dict = rest_v10_specification_sections_post_request_instance.to_dict()
# create an instance of RestV10SpecificationSectionsPostRequest from a dict
rest_v10_specification_sections_post_request_from_dict = RestV10SpecificationSectionsPostRequest.from_dict(rest_v10_specification_sections_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


