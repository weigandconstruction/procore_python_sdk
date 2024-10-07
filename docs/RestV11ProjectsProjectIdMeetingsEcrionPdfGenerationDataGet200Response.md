# RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pdf_template** | [**RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponsePdfTemplate**](RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponsePdfTemplate.md) |  | [optional] 
**meetings** | [**List[RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner]**](RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response import RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response from a JSON string
rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_instance = RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_dict = rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response from a dict
rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_from_dict = RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response.from_dict(rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


