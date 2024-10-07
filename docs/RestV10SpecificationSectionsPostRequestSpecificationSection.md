# RestV10SpecificationSectionsPostRequestSpecificationSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | 
**description** | **str** |  | [optional] 
**specification_section_division_id** | **int** | The ID of the parent Specification Section Division | 

## Example

```python
from procore_sdk.models.rest_v10_specification_sections_post_request_specification_section import RestV10SpecificationSectionsPostRequestSpecificationSection

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SpecificationSectionsPostRequestSpecificationSection from a JSON string
rest_v10_specification_sections_post_request_specification_section_instance = RestV10SpecificationSectionsPostRequestSpecificationSection.from_json(json)
# print the JSON string representation of the object
print(RestV10SpecificationSectionsPostRequestSpecificationSection.to_json())

# convert the object into a dict
rest_v10_specification_sections_post_request_specification_section_dict = rest_v10_specification_sections_post_request_specification_section_instance.to_dict()
# create an instance of RestV10SpecificationSectionsPostRequestSpecificationSection from a dict
rest_v10_specification_sections_post_request_specification_section_from_dict = RestV10SpecificationSectionsPostRequestSpecificationSection.from_dict(rest_v10_specification_sections_post_request_specification_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


