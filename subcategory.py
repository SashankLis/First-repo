def subcategory_load():

            #       subcategory

        # truncate tmp table SUBCATEGORY

        # truncate_tmp_subcategory = '''
            #                              TRUNCATE TABLE BHATBHATENI.SASHANK_TMP.TMP_SUBCATEGORY
            #                             '''

            # sf.execute_query(truncate_tmp_subcategory)


        # load tmp table SUBCATEGORY


            load_temp_subcategory = '''
                                        INSERT INTO BHATBHATENI.SASHANK_TMP.TMP_SUBCATEGORY(
                                        SUB_CTGRY_ID,CTGRY_KY,SUB_CTGRY_DESC
                                        )
                                        SELECT ID,CTGRY.CTGRY_KY,SUBCATEGORY_DESC
                                        FROM BHATBHATENI.SASHANK_STG.STG_SUBCATEGORY SUBCTGRY
                                        LEFT JOIN BHATBHATENI.SASHANK_TGT.TGT_CATEGORY CTGRY
                                        ON SUBCTGRY.CATEGORY_ID = CTGRY.CTGRY_ID;
                                        '''
            sf.execute_query(load_temp_subcategory)


            # load target table SUBCATEGORY

            load_tgt_subcategory = '''
                                            INSERT INTO BHATBHATENI.SASHANK_TGT.TGT_SUBCATEGORY(
                                            SUB_CTGRY_KY,SUB_CTGRY_ID,CTGRY_KY,SUB_CTGRY_DESC,OPEN_CLOSE_CD,ROW_INSRT_TMS,ROW_UPDT_TMS
                                            )
                                            SELECT SUB_CTGRY_KY,SUB_CTGRY_ID, CTGRY_KY, SUB_CTGRY_DESC,
                                            1,LOCALTIMESTAMP,LOCALTIMESTAMP
                                            FROM BHATBHATENI.SASHANK_TMP.TMP_SUBCATEGORY
                                            WHERE SUB_CTGRY_ID NOT IN (SELECT DISTINCT SUB_CTGRY_ID FROM BHATBHATENI.SASHANK_TGT.TGT_SUBCATEGORY)
                                            '''
            sf.execute_query(load_tgt_subcategory)

    # update target table SUBCATEGORY


            # update_tgt_subcategory = '''
            #                                 UPDATE BHATBHATENI.SASHANK_TGT.TGT_SUBCATEGORY T1
            #                                 SET T1.CTGRY_KY = T2.CTGRY_KY,
            #                                 T1.SUB_CTGRY_DESC = T2.SUB_CTGRY_DESC,
            #                                 ROW_UPDT_TMS = LOCALTIMESTAMP
            #                                 FROM BHATBHATENI.SASHANK_TMP.TMP_SUBCATEGORY T2
            #                                 WHERE T1.SUB_CTGRY_ID = T2.SUB_CTGRY_ID;
            #                                 '''
            # sf.execute_query(update_tgt_subcategory)



