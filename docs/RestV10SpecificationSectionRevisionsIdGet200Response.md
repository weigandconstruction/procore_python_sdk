# RestV10SpecificationSectionRevisionsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**source_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**section_id** | **int** |  | [optional] 
**section_name** | **str** |  | [optional] 
**source_create_time** | **datetime** |  | [optional] 
**source_update_time** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_specification_section_revisions_id_get200_response import RestV10SpecificationSectionRevisionsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SpecificationSectionRevisionsIdGet200Response from a JSON string
rest_v10_specification_section_revisions_id_get200_response_instance = RestV10SpecificationSectionRevisionsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10SpecificationSectionRevisionsIdGet200Response.to_json())

# convert the object into a dict
rest_v10_specification_section_revisions_id_get200_response_dict = rest_v10_specification_section_revisions_id_get200_response_instance.to_dict()
# create an instance of RestV10SpecificationSectionRevisionsIdGet200Response from a dict
rest_v10_specification_section_revisions_id_get200_response_from_dict = RestV10SpecificationSectionRevisionsIdGet200Response.from_dict(rest_v10_specification_section_revisions_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


