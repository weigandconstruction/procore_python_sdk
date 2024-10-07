# RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponsePdfTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | uuid of the PdfTemplate | [optional] 
**pdf_filename** | **str** | Filename of the PdfTemplate | [optional] 
**name** | **str** | Name of the PdfTemplate | [optional] 
**url** | **str** | url of the PdfTemplate | [optional] 
**storage_type** | **str** | The storage type for the pdf to be passed to ecrion. Should be govcloud or default. | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_pdf_template import RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponsePdfTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponsePdfTemplate from a JSON string
rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_pdf_template_instance = RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponsePdfTemplate.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponsePdfTemplate.to_json())

# convert the object into a dict
rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_pdf_template_dict = rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_pdf_template_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponsePdfTemplate from a dict
rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_pdf_template_from_dict = RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponsePdfTemplate.from_dict(rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_pdf_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


